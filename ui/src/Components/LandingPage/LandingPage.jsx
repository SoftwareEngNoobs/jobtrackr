import React, { useEffect, useState } from 'react';
import { Button, Card, Tag, Typography } from 'antd';
import { EditFilled, PlusOutlined } from '@ant-design/icons';
import axios from 'axios';
import { useLocation } from 'react-router-dom';
import config from '../../config';
import AddApplication from '../AddApplication/AddApplication';
import EditApplication from '../AddApplication/EditApplication';
import './LandingPage.scss';
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';
import ApplicationCard from '../AddApplication/ApplicationCard';

const columns = {
	applied: 'Applied',
	inReview: 'In Review',
	interview: 'Interview',
	decision: 'Decision',
};

export default function LandingPage() {
	const [applications, setApplications] = useState([]);
	const [loading, setLoading] = useState(true);
	const [addApplicationOpen, setAddApplicationOpen] = useState(false);
	const [editApplication, setEditApplication] = useState(false);
	const { state } = useLocation();

	const quickUpdateApplications = (application, updatedValue) => {
		axios
			.post(`${config.base_url}/modify_application`, {
				companyName: application.companyName,
				jobTitle: application.jobTitle,
				jobId: application.jobId,
				description: application.description,
				url: application.url,
				date: application.date,
				status: updatedValue,
				image: application.image,
				_id: application._id,
				email: state.email,
			})
			.then(({ data }) => {
				message.success(data.message);
				refresh();
			})
			.catch((err) => message.error(err.response.data?.error));
	};

	const handeDragEnd = (result) => {
		if (!result.destination) {
			return;
		}
		const { source, destination } = result;
		if (source.droppableId != destination.droppableId) {
			var i = 0;
			for (var app of applications) {
				if (app._id == result.draggableId) {
					if (destination.droppableId == '0') {
						app.status = 'applied';
						applications[i] = app;
						setApplications(applications);
						quickUpdateApplications(app, 'applied');
					} else if (destination.droppableId == '1') {
						app.status = 'inReview';
						applications[i] = app;
						setApplications(applications);
						quickUpdateApplications(app, 'inReview');
					} else if (destination.droppableId == '2') {
						app.status = 'interview';
						applications[i] = app;
						setApplications(applications);
						quickUpdateApplications(app, 'interview');
					} else {
						app.status = 'accepted';
						applications[i] = app;
						setApplications(applications);
						quickUpdateApplications(app, 'accepted');
					}
				}
				i += 1;
			}
		}
	};

	useEffect(() => {
		updateApplications();
	}, []);

	const updateApplications = () => {
		axios
			.get(`${config.base_url}/view_applications?email=` + state.email)
			.then(({ data }) => setApplications(data.applications))
			.catch((err) => console.log(err))
			.finally(() => setLoading(false));
	};

	const toggleAddApplication = () => setAddApplicationOpen(!addApplicationOpen);
	return (
		<div className="LandingPage">
			<div className="SubHeader">
				<div className="flex" />
				<Button
					id="add-application"
					type="primary"
					size="large"
					icon={<PlusOutlined />}
					onClick={toggleAddApplication}
				>
					Add Application
				</Button>
				<AddApplication
					isOpen={addApplicationOpen}
					onClose={toggleAddApplication}
					updateApplications={updateApplications}
				/>
			</div>

			<div className="MainContent">
				<DragDropContext onDragEnd={handeDragEnd}>
					{Object.keys(columns).map((col, index) => (
						<Droppable droppableId={String(index)} key={index}>
							{(provided) => (
								<div
									className="Status"
									key={col}
									{...provided.droppableProps}
									ref={provided.innerRef}
								>
									<Typography.Title level={5}>{columns[col]}</Typography.Title>
									{loading ? (
										<>
											<Card loading bordered={false} />
											<Card loading bordered={false} />
											<Card loading bordered={false} />
										</>
									) : (
										applications.map(
											(application, index) =>
												(application.status === col ||
													(col === 'decision' &&
														['rejected', 'accepted'].includes(
															application.status
														))) && (
													<Draggable
														key={application._id}
														draggableId={application._id}
														index={index}
													>
														{(provided) => (
															<div
																{...provided.draggableProps}
																ref={provided.innerRef}
																{...provided.dragHandleProps}
															>
																<ApplicationCard
																	key={col + index}
																	application={application}
																	modalFunc={setEditApplication}
																	refresh={updateApplications}
																	email={state.email}
																/>
															</div>
														)}
													</Draggable>
												)
										)
									)}
									{applications.length === 0 && 'No applications found.'}
									{provided.placeholder}
								</div>
							)}
						</Droppable>
					))}
				</DragDropContext>
			</div>
			{editApplication && (
				<EditApplication
					application={editApplication}
					onClose={() => setEditApplication(false)}
					updateApplications={updateApplications}
					email={state.email}
				/>
			)}
		</div>
	);
}
