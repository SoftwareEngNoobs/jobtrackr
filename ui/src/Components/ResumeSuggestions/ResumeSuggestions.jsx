import React, { useEffect, useState } from 'react';
import { Button, Card, Tag, Typography } from 'antd';
import axios from 'axios';
import { useLocation } from 'react-router-dom';
import { DownloadOutlined } from '@ant-design/icons';
import { PlusOutlined } from '@ant-design/icons';
import config from '../../config';
import './ResumeSuggestions.scss';
import { MakeSuggestions } from './MakeSuggestions';

export function ResumeSuggestions() {
	const [resumeSuggestion, setResumeSuggestion] = useState('');
	const [makeResumeSuggestionOpen, setResumeSuggestionOpen] = useState(false);
	const [matchSkills, updateMatchSkills] = useState([]);
	const [missSkills, updateMissSkills] = useState([]);
	const [score, updateScore] = useState(0);

	useEffect(() => {
		updateResumeSuggestion('');
	}, []);
	const updateResumeSuggestion = (content) => {
		setResumeSuggestion(content);
	};
	const toggleMakeResumeSuggestion = () => setResumeSuggestionOpen(!makeResumeSuggestionOpen);
	const getSuggestion = () => {
		const url = window.URL.createObjectURL(
			new Blob([resumeSuggestion], { type: 'text/plain' })
		);
		const link = document.createElement('a');
		link.href = url;
		link.setAttribute('download', 'resume_suggestions.txt');
		document.body.appendChild(link);
		link.click();
		document.body.removeChild(link);
	};
	return (
		<div className="ResumeSuggestion">
			<div className="SubHeader">
				<div className="flex" />
				<div className="SubHeader">
					<div className="flex" />
					<Button
						id="generate-suggestions"
						type="primary"
						size="large"
						icon={<PlusOutlined />}
						onClick={toggleMakeResumeSuggestion}
					>
						Generate Resume Suggestions
					</Button>
					<MakeSuggestions
						isOpen={makeResumeSuggestionOpen}
						onClose={toggleMakeResumeSuggestion}
						updateSuggestions={updateResumeSuggestion}
						updateMatchedSkills={updateMatchSkills}
						updateMissingSkills={updateMissSkills}
						updateATSScore={updateScore}
					/>
				</div>
			</div>

			<div className="ResumeSuggest">
				<Card className="ResumeCard" key={1} title={'Resume Suggestions'}>
					{resumeSuggestion}
					{resumeSuggestion.length > 0 && (
						<>
							<Typography.Title level={5} style={{ marginTop: '10px' }}>
								Matched Skills:
							</Typography.Title>
							{matchSkills.map((value) => {
								return (
									<Button
										type="primary"
										color="primary"
										style={{
											borderRadius: '15px',
											marginBottom: '10px',
											marginRight: '5px',
											padding: '0 10px 0 10px',
										}}
										size="small"
										variant="filled"
									>
										{value}
									</Button>
								);
							})}
							<Typography.Title level={5}>Missing Skills:</Typography.Title>
							{missSkills.map((value) => {
								return (
									<Button
										type="danger"
										style={{
											borderRadius: '15px',
											marginBottom: '10px',
											marginRight: '5px',
											padding: '0 10px 0 10px',
										}}
										size="small"
										color="danger"
										variant="filled"
									>
										{value}
									</Button>
								);
							})}
							<Typography.Title level={5}>ATS Score:</Typography.Title>
							<Button
								style={{
									borderRadius: '15px',
									marginBottom: '10px',
									padding: '0 10px 0 10px',
								}}
								size="small"
								type="default"
								color="default"
								variant="filled"
							>
								{score}
							</Button>
						</>
					)}
					{resumeSuggestion.length > 0 && (
						<>
							<br />
							<Button
								id="download"
								type="primary"
								size="large"
								icon={<DownloadOutlined />}
								onClick={getSuggestion}
							>
								Download
							</Button>
						</>
					)}
				</Card>
			</div>
		</div>
	);
}
