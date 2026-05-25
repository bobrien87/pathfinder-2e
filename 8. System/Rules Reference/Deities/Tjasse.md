---
type: deity
source-type: "Remaster"
domains: "Air, Destruction, Might, Nature"
favored-weapon: "Spear"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Animal Allies]], Rank 3: [[Haste]], Rank 4: [[Aerial Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Tjasse, the father of Skode, is the cloud giant god and lord of rocs, wind, and high mountain peaks. He is credited for taming rocs to serve cloud giants and possessing shapeshifting abilities second only to Skrymir (much to his chagrin). Stories of his incredible arrogance precede him and most of his accolades, closely followed by cautionary tales of those unfortunate enough to have provoked his ire. The only thing that surpasses his vanity is his love for Skode, and the only thing greater than the wrath incurred by those who cross him is the destructive force he unleashes upon those who wrong his daughter. The Lord of Talons is a colossal being, dwarfing many members of the giant pantheon in comparison. He is always described as strikingly beautiful, though the exact details of his appearance change frequently.

**Title** Lord of Talons

**Areas of Concern** Giant birds, mountain peaks, pride

**Edicts** Only ever hunt birds for food, aggressively oppose those who do not have your best interest at heart, protect your children at all cost

**Anathema** Harm birds for sport or via negligence, bow down to your oppressor, show mercy to anyone who wronged your child

**Religious Symbol** mountain gripped by talons

**Sacred Animal** roc

**Sacred Colors** gray, red

**Source:** `= this.source` (`= this.source-type`)
