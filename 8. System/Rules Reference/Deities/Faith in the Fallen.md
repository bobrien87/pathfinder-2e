---
type: deity
source-type: "Remaster"
domains: "Cities, Fate, Sorrow, Vigil"
favored-weapon: "Glaive"
divine-font: "Harm, Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Jump]], Rank 4: [[Translocate]], Rank 6: [[Cast Into Time]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Since the inception of the Test of the Starstone, dozens if not hundreds of aspirants have tried, and failed, to ascend beyond the realm of mortality. Some are more notable than others: Gobru, Speaker for the Bountiful Sea; Silmor, Lord of Blades; Oggo, Master of the Sixteen Poses; and the Muted God, to name a few. Some even briefly retained cults in their names, who continued to offer their worship passed the supposed deaths of their patrons.

Following several recent events—the appearance of New Thassilon plucked out of time and the closure of the Worldwound—new attention has been given to lingering divine mysteries once thought to not be possible. As is often the case when involving tales of the Starstone, awareness has given way to faith in those who have fallen. This covenant has broad appeal to many whose belief structures fall outside that of more mainstream churches or pantheons, and it often draws its adherents to the city at the center of the world.

Whether the divine power that comes from worshipping this covenant comes from a handful of failed Test of the Starstone aspirants or from some other, more sinister, source has yet to be determined.

**Covenant Members** unknown; possibly the spirits of those who failed the Test of the Starstone or even the Starstone itself

**Areas of Concern** aspiring divinities, citizens of Absalom, the downtrodden, the homeless

**Edicts** embody the best aspects of those who risked their souls to seek divinity, respect and remember the sacrifice of others, seek out and aid those on the verge of divinity

**Anathema** allow the deceased to be forgotten, dismiss another's beliefs no matter how strange they might seem, fail to aid others once you have promised to do so

**Religious Symbol** ghostly hand clutching a glowing stone

**Source:** `= this.source` (`= this.source-type`)
