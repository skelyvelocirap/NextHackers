import Link from "next/link";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "./ui/card";
import SkillTag from "./skill-tag";
import Image from "next/image";
import { skills as allSkills } from "@/lib/dummy-data";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "./ui/dialog";
import { Button } from "./ui/button";

export default function ProfileCard({
  name,
  title,
  image,
  skills,
  id,
  bio,
  volunteerHours,
}) {
  const userSkills = skills
    .map((skillId) => allSkills.find((skill) => skill.skillId === skillId))
    .filter((skill) => skill !== undefined); // Filter out undefined skills

  return (
    <Dialog>
      <DialogTrigger>
        <Card className="hover:scale-[103%] transition-all duration-200 ease-out hover:shadow-lg h-full flex flex-col justify-between items-center">
          <CardHeader className="flex flex-col gap-1 justify-start items-center text-center">
            <div className="relative size-20 rounded-full bg-slate-400 shadow-inner overflow-hidden">
              <Image
                className="absolute object-cover"
                fill
                src={image}
                alt={name}
              />
            </div>
            <div>
              <CardTitle className="text-lg font-semibold">{name}</CardTitle>
              <CardDescription>{title}</CardDescription>
            </div>
          </CardHeader>
          <CardContent>
            {userSkills && (
              <div className="flex flex-wrap gap-2">
                {userSkills.map((skill) => (
                  <SkillTag key={skill.skillId} varient="small">
                    {skill.skillName}
                  </SkillTag>
                ))}
              </div>
            )}
          </CardContent>
        </Card>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <div className="flex flex-col items-center gap-4 justify-center p-6 max-w-xl mx-auto">
            <div className="flex flex-col justify-center items-center gap-4 text-center">
              <div className="relative size-24 rounded-full bg-slate-400 shadow-inner overflow-hidden">
                <Image
                  className="absolute object-cover"
                  fill
                  src={image}
                  alt={name}
                />
              </div>
              <div>
                <DialogTitle className="font-semibold text-lg">
                  {name}
                </DialogTitle>
                <p className="text-sm mb-4">{title}</p>
                <p className="mb-6">{bio}</p>
              </div>
            </div>
            <div className="mb-6">
              <h3 className="font-semibold text-center mb-4">
                Skills I teach:
              </h3>
              <ul>
                {userSkills && (
                  <div className="flex flex-wrap gap-2">
                    {userSkills.map((skill) => (
                      <SkillTag key={skill.skillId} varient="small">
                        {skill.skillName}
                      </SkillTag>
                    ))}
                  </div>
                )}
              </ul>
            </div>
            <div className="flex justify-center items-center gap-4">
              <Button>Book session</Button>
              <Button variant="outline">Message</Button>
            </div>
          </div>
        </DialogHeader>
      </DialogContent>
    </Dialog>
  );
}
