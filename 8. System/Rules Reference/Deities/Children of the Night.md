---
type: deity
source-type: "Remaster"
domains: "Darkness, Indulgence, Secrecy, Undeath"
favored-weapon: "Rapier"
divine-font: "Harm"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Illusory Disguise]], Rank 3: [[Wall Of Shadow]], Rank 7: [[Shadow Raid]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Trust is the last thing you would assume to find at the heart of a pantheon of wicked, murderous gods, but for those who are part of the Children of the Night, it is paramount. As much as these gods might distrust one another, they understand that sometimes such trepidations must be overcome for a greater goal. For this tenuously connected group of immortal powers, that goal is to work together to protect their followers, usually beings who must, at all costs, protect their true natures: assassins, vampires, werewolves, and other creatures of the shadows.

**Pantheon Members** Camazotz, Nin, Urgathoa, Yaezhing, Zura

**Areas of Concern** assassination, secrecy, self-preservation through murder, vampires

**Edicts** deal a suitable demise to enemies of the faith, do not allow others to see who you truly are, put your needs above others

**Anathema** give to others more than what you have for yourself, willingly reveal secrets about vampires

**Religious Symbol** bat wing with a bloody claw

**Source:** `= this.source` (`= this.source-type`)
