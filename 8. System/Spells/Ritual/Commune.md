---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "6"
traits: ["[[Prediction]]"]
cast: "1 day"
duration: "up to 10 minutes"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call upon an unknown, powerful being to answer questions. The being varies depending on the skill used for the primary check.

- **Nature** Primal spirits of nature, which know about animals, beasts, fey, fungi, plants, topography, and natural resources within a 3-mile radius.
- **Occultism** Planar and other mysterious entities such as elementals, forgotten spirits, and monitors, which know about forgotten knowledge, the planes, obscure secrets, and other esoterica.
- **Religion** Divine beings like celestials and fiends that know about the gods they serve and the god's respective purview; these are typically a servitor of your deity if you have one.

You can ask up to seven questions that could be answered with "Yes" or "No." The entity answers with one-word answers such as "Yes," "No," "Likely," and "Unknown," though its answers always reflect its own agenda and could be deceptive.
- **Critical Success** You contact a more powerful entity aligned strongly with your interests, possibly even your deity. The entity won't attempt to deceive you, though it still might not know the answers. When it's important to provide clarity, the entity will answer your questions with up to five words, such as "If you leave immediately" or "That was true once."
- **Success** You can ask your questions and receive answers.
- **Failure** You fail to contact an appropriate being.
- **Critical Failure** You are exposed to the enormity of the cosmos and are [[Stupefied 4]] for 1 week (can't remove by any means).

**Source:** `= this.source` (`= this.source-type`)
