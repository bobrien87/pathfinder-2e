---
type: deity
source-type: "Remaster"
domains: "Dreams, Fate, Repose, Time"
favored-weapon: "Dagger"
divine-font: "Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Sleep]], Rank 2: [[Shrink]], Rank 5: [[Stagnate Time]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Atropos, known among the psychopomp ushers as the Judge of Judges and the Last Sister, is Pharasma's youngest (and perhaps only) daughter, ruling over the Boneyard alongside her mother as the penultimate arbiter of mortal fates. The psychopomp manifests as a large nosoi with a shimmering, silver mask and a long tail of vivid peacock feathers, each bearing a living mortal eye: one feather with one eye for every soul past, present, and future to receive her judgment. When appearing in mortal guise, Atropos instead takes the form of a young human girl, and she often favors this form during appearances in her mother's court.

**Title** The Judge of Judges

**Areas of Concern** Fate, sleep, youth

**Edicts** Mentor the next generation, study and learn from failure, heed the insights of dreams and sleepless visions

**Anathema** Disturb the weary from rest, allow harm to come to children, create undead

**Religious Symbol** six overlapping lines arranged in a hexagon

**Sacred Animal** nightengale

**Sacred Colors** silver

**Source:** `= this.source` (`= this.source-type`)
