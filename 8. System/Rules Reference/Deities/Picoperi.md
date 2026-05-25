---
type: deity
source-type: "Remaster"
domains: "Change, Confidence, Delirium, Trickery"
favored-weapon: "Blowgun"
divine-font: "Heal"
divine-skill: "Acrobatics"
divine-spells: "Rank 1: [[Grease]], Rank 3: [[Feet To Fins]], Rank 6: [[Mislead]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Picoperi, the eternal trickster, finds joy in even the simplest joke or prank. He delights in the surprises of daily life, always seeking the next thrill. Never content with regular schedules, his days vary wildly from one to the next. One evening, he may try to tickle Asmodeus's nose with a feather and the next morning, he may bump Artokus Kirran's arm as the famous alchemist works in his lab. No one is too important or mundane for his jests.

Those who in need of a little luck often call upon Picoperi for aid. When formulating new rituals, arcane practitioners ask him to guide their hands in selecting metal powders for their binding rings. Alchemists whisper an oath to him as they mix volatile compounds. Many a discovery has been made when two reagents were swapped with an appreciative cry of "Thank Merrygleam!" Equally, disasters come with a groan and a request for Picoperi to take his mischief elsewhere for a while.

**Title** Merrygleam

**Areas of Concern** Jokes, pranks, and surprises

**Edicts** Relish in jokes and pranks, lighten the mood, embrace surprises

**Anathema** Spoil the fun, use a prank to cause real harm

**Religious Symbol** Snake on a tree branch

**Sacred Animal** tree snake

**Sacred Colors** brown, green

**Source:** `= this.source` (`= this.source-type`)
