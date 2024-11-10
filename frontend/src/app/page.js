import Footer from "@/components/footer";
import Navbar from "@/components/navbar";
import ProfileCard from "@/components/profile-card";
import SkillTag from "@/components/skill-tag";
import { skills, users } from "@/lib/dummy-data";

export default function Home() {
  return (
    <div className="">
      <section className="section pt-40">
        <div className="flex flex-col justify-center items-center text-center max-w-2xl mx-auto">
          <h1 className="heading-1 mb-6">
            Learn to code with free one-on-one mentorship.
          </h1>
          <p className="mb-10">
            KnowledgeHub is an online platform designed to connect individuals
            who want to learn specific skills with those who are willing to
            teach them.
          </p>
          <p className="mb-4 font-semibold">I want to learn...</p>
          <div className="flex flex-wrap gap-2 justify-center items-center max-w-2xl">
            {skills.map((skill) => (
              <SkillTag key={skill.skillId}>{skill.skillName}</SkillTag>
            ))}
          </div>
        </div>
      </section>
      <section className="section">
        <div className="grid grid-cols-4 gap-6">
          {users.map((user) => (
            <ProfileCard
              key={user.id}
              name={user.name}
              title={user.title}
              image={user.profilePic}
              skills={user.skills}
            />
          ))}
        </div>
      </section>
    </div>
  );
}
