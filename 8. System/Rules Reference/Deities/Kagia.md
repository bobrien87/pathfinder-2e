---
type: deity
source-type: "Remaster"
domains: "Death, Nature, Repose, Vigil"
favored-weapon: "Sickle"
divine-font: "Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Sleep]], Rank 2: [[Animal Form]], Rank 6: [[Tangling Creepers]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Kagia takes the form of a hulking bear with two vulture heads. Though not a true deity, he is likely the closest among living spirit guides to claiming that ascendance. His half-brother, Dolok Darkfur, is also a contender, but Dolok's long period of inactivity has likely left the feathered bear with a smaller number of mortal followers and less interest in growing his spiritual power. As the only child ever born to Bear and Vulture (whose relationship lasted only a few mortal generations when clans they protected regularly intermarried), Kagia possesses immense physical power. Though he is easily roused to anger, the burly deity is most concerned with the collection of resources and their efficient use. Berry picking is sacred to him, and artisans work his image into the bottom of finely woven baskets in hopes of a bountiful harvest. His worshippers value self-sufficiency, and avoid wearying Kagia with petty requests, lest he drop into a torpor and leave them undefended. Priests of Kagia handle the interning of the dead, and they gather and redistribute the belongings of the deceased in a way that benefits the clan as a whole.

**Title** He Gathers In

**Areas of Concern** Efficiency, harvests, resourcefulness

**Edicts** Dispose of the dead, take appropriate time to rest, sustainably harvest resources

**Anathema** Kill for pleasure or glory, waste resources

**Religious Symbol** basket overflowing with berries

**Sacred Animal** bear

**Sacred Colors** brown, yellow

**Source:** `= this.source` (`= this.source-type`)
