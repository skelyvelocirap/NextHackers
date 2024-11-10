"use client";
import { useState } from "react";
import ProfileCard from "@/components/profile-card";
import SkillTag from "@/components/skill-tag";
import { skills, users } from "@/lib/dummy-data";

export default function Home() {
  const [selectedSkillId, setSelectedSkillId] = useState(null); // Track selected skill ID

  // Function to handle skill tag click
  const handleSkillClick = (skillId) => {
    if (selectedSkillId === skillId) {
      setSelectedSkillId(null); // Unselect if the same skill is clicked
    } else {
      setSelectedSkillId(skillId); // Select the new skill
    }
  };

  // Filter users based on selected skill
  const filteredUsers = selectedSkillId
    ? users.filter((user) => user.skills.includes(selectedSkillId))
    : users; // Show all users if no skill is selected

  return (
    <div>
      <section className="section">
        <div className="flex flex-col justify-center items-center text-center max-w-2xl mx-auto">
          <h1 className="text-5xl font-bold mb-6">
            Learn to code with free{" "}
            <span className="text-nowrap">one-on-one</span> mentorship.
          </h1>
          <p className="mb-10">
            KnowledgeHub is an online platform designed to connect individuals
            who want to learn specific skills with those who are willing to
            teach them.
          </p>
          <p className="mb-4 font-semibold">I want to learn...</p>
          <div className="flex flex-wrap gap-2 justify-center items-center max-w-2xl">
            {skills.map((skill) => (
              <SkillTag
                key={skill.skillId}
                onClick={() => handleSkillClick(skill.skillId)}
                isSelected={selectedSkillId === skill.skillId}
              >
                {skill.skillName}
              </SkillTag>
            ))}
          </div>
        </div>
      </section>
      <section className="section">
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {filteredUsers.map((user) => (
            <ProfileCard
              key={user.id}
              name={user.name}
              title={user.title}
              image={user.profilePic}
              skills={user.skills}
              id={user.id}
              bio={user.bio}
              volunteerHours={user.volunteerHours}
            />
          ))}
        </div>
      </section>
    </div>
  );
}
