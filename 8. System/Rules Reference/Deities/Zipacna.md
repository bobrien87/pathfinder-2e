---
type: deity
source-type: "Remaster"
domains: "Earth, Indulgence, Fire, Might"
favored-weapon: "Spear"
divine-font: "Harm"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Shockwave]], Rank 3: [[Shifting Sand]], Rank 5: [[Telekinetic Haul]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The lazy but violent Zipacna is one the largest sahkil tormentors, resembling a massive caiman with four eyes and unnervingly human hands. He prefers to lounge in the lusher regions of Xibalba being pampered by the unfortunate souls he's forcefully inducted into his service, doling out vicious punishments when his demands aren't met. Even the other sahkil tormentors avoid testing his fury, as his penchant for destructive violence overwhelms everything in his path.

**Title** The Mountain Below

**Areas of Concern** Avoiding responsibility, shifting earth, violence

**Edicts** Do only what you must, eat your fill, overpower anyone who challenges you

**Anathema** Serve others, allow laziness to create more work for yourself, refuse an indulgence

**Religious Symbol** stylized mountain, one half of which is crumbling

**Sacred Animal** boar

**Sacred Colors** brown, gold

**Source:** `= this.source` (`= this.source-type`)
