import React, { useEffect, useState } from 'react';
import { PlusOutlined, DownloadOutlined } from '@ant-design/icons';
import { Button, Card, Empty, Select } from 'antd';
import './Coverletter.scss';
import { useLocation } from 'react-router-dom';
import MakeCoverLetter from './MakeCoverLetter';
import ReactMarkdown from 'react-markdown';
import jsPDF from 'jspdf';

const { Option } = Select;

export default function Coverletter() {
	const [coverLetter, setCoverLetter] = useState("");
	const [makeCoverLetterOpen, setCoverLetterOpen] = useState(false);
	const [downloadFormat, setDownloadFormat] = useState("md"); // Default format is Markdown
	const { state } = useLocation();

	useEffect(() => {
		updateCoverLetter("");
	}, []);

	const updateCoverLetter = (letter) => {
		setCoverLetter(letter);
	};

	const toggleMakeCoverLetter = () => setCoverLetterOpen(!makeCoverLetterOpen);

	const downloadCoverLetter = () => {
		
			// For Markdown or Text formats
			const blobType = downloadFormat === "md" ? "text/markdown" : "text/plain";
			const fileExtension = downloadFormat === "md" ? "md" : "txt";

			const url = window.URL.createObjectURL(new Blob([coverLetter], { type: blobType }));
			const link = document.createElement("a");
			link.href = url;
			link.setAttribute("download", `cover_letter.${fileExtension}`);
			document.body.appendChild(link);
			link.click();
			document.body.removeChild(link);
		
	};

	return (
		<div className="CoverLetter">
			<div className="SubHeader">
				<Button
					id="generate-cv"
					type="primary"
					size="large"
					icon={<PlusOutlined />}
					onClick={toggleMakeCoverLetter}
				>
					Generate Cover Letter
				</Button>
				<MakeCoverLetter
					isOpen={makeCoverLetterOpen}
					onClose={toggleMakeCoverLetter}
					updateCoverLetter={updateCoverLetter}
				/>
			</div>
			<div className="CV">
				<Card className="CVCard" key={1} title={"Cover Letter"}>
					{coverLetter.length > 0 ? (
						<>
							<ReactMarkdown>{coverLetter}</ReactMarkdown>
							<br />
							<Select
								value={downloadFormat}
								onChange={setDownloadFormat}
								style={{ width: 150, marginRight: 10 }}
							>
								<Option value="md">Markdown (.md)</Option>
								<Option value="txt">Plain Text (.txt)</Option>
								
							</Select>
							<Button
								id="download"
								type="primary"
								size="large"
								icon={<DownloadOutlined />}
								onClick={downloadCoverLetter}
							>
								Download
							</Button>
						</>
					) : (
						<Empty description="No cover letter generated yet" />
					)}
				</Card>
			</div>
		</div>
	);
}
