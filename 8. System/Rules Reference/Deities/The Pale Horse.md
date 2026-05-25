---
type: deity
source-type: "Remaster"
domains: "Death, Duty, Pain, Repose"
favored-weapon: "Trident"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Phantom Pain]], Rank 2: [[Feral Shades]], Rank 3: [[Ghostly Weapon]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Pale Horse stalks the banks of the River of Souls. This has been true for eons, though few things are immune to change, and the story of the Pale Horse is no exception. Long ago, the stories say, a daemon traveled the pathways between the planes, consuming the souls of the dead before they reached the Lady of Graves. He appeared as a silent white stallion, and his name was the Pale Horse. Now, they speak of a psychopomp usher who guards mortal souls while they journey into the afterlife, hunting any who dare steal from the River of Souls. His name is the Pale Horse, and he serves the Gray Lady.

**Title** The Lash and the Plough

**Areas of Concern** Beasts of burden, duty, revenge

**Edicts** Aid and be of service to friends and allies, fulfill your duties, seek vengeance

**Anathema** Break an oath, cower from combat, damage or destroy a soul, show mercy to those who betray you

**Religious Symbol** horizontal line with a circle and three dots at one end

**Sacred Animal** horse

**Sacred Colors** white

**Source:** `= this.source` (`= this.source-type`)
