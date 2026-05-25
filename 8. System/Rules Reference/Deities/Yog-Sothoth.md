---
type: deity
source-type: "Remaster"
domains: "Knowledge, Void, Time, Travel"
favored-weapon: "Dagger"
divine-font: "Harm"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Fleet Step]], Rank 5: [[Slither]], Rank 7: [[Time Beacon]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Yog-Sothoth is, along with Azathoth, one of the greatest of the Outer Gods. In appearance, he is said to be a congeries of iridescent spheres-brilliant, foaming bubbles that constantly expand and collapse in upon themselves. He has other manifestations, however, including the Lurker on the Threshold, a mass of black tentacles that endlessly writhe, reach, and grow, and a mysterious humanoid figure hidden behind a shimmering veil.

Yog-Sothoth embodies all of space and time; he exists in all places and in all moments simultaneously. Paradoxically, however, he is unable to manifest in the mortal universe unless summoned, a magical act that almost always results in untold destruction. He is known as the Key and the Gate, and magicians and cults research him in an effort to master time and space. Fortunately, his worship is not widespread, but some of those who have delved deep into his secrets describe him as an ambivalent figure, rather than a malevolent one, who guards cosmic secrets and makes them accessible to those who dare to ask for them. Yog-Sothoth reveals the true nature of the universe, but this is a thing that once seen cannot be unseen, and wise mortals turn aside from Yog-Sothoth's offer of cosmic knowledge in favor of a more mundane existence.

**Title** Lurker at the Threshold

**Areas of Concern** Gates, space, time

**Edicts** Gather knowledge of gates through space and time, curse or mutate unborn children

**Anathema** None

**Religious Symbol** black spiral

**Sacred Animal** none

**Sacred Colors** none

**Source:** `= this.source` (`= this.source-type`)
