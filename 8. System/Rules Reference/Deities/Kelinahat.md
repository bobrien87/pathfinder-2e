---
type: deity
source-type: "Remaster"
domains: "Confidence, Knowledge, Secrecy, Trickery"
favored-weapon: "Shortsword"
divine-font: "Heal"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Vanishing Tracks]], Rank 4: [[Ocular Overload]], Rank 6: [[Mislead]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

While most gods prefer to be easily found by those that would worship them, Kelinahat prefers to stay out of the limelight, sticking to the shadows where she is most likely to hear that which others would not. When she wraps her smoky black wings around her slight frame, she is almost impossible to see except in the brightest of sunlight. Even then, she resembles only the vaguest shape of a winged dwarven woman made entirely of shadow and difficult to discern, as if one's eyes refuse to focus on her. She uses this ability to hide in places of torment and torture, working to find information that can be used to free those who have been wrongfully imprisoned. Once she has this, she ensures it makes it to the eyes and ears of those who can use it, keeping herself just as invisible, not wanting others to know where the intelligence came from.

**Title** She of Ebon Wings

**Areas of Concern** Intelligence, spies, stealth

**Edicts** Gather valuable intelligence, train in the art of espionage, use information you learn to free the innocent

**Anathema** Throw away useful information, destroy evidence of wrongdoing, willingly give information to those of evil intent

**Religious Symbol** shortsword and moon

**Sacred Animal** bat

**Sacred Colors** black, light blue

**Source:** `= this.source` (`= this.source-type`)
