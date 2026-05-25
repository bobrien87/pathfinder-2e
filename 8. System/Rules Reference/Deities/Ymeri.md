---
type: deity
source-type: "Remaster"
domains: "Destruction, Dust, Fire, Zeal"
favored-weapon: "Longsword"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 2: [[Summon Elemental]], Rank 4: [[Wall Of Fire]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Ymeri, Queen of the Inferno, holds dominion over fire, heat, and smoke. Ymeri governs from her Auroric Palace, taking the form of a six-armed reptilian centaur with burning wings. She has systematically destroyed all record of her birth and true origins, and she wages a never-ending war against the other denizens of the Plane of Fire and against the jabalis of the Plane of Earth. Of all the elemental lords, Ymeri has the largest following. Some scamps and many fire elementals revere her, alongside some ifrits and a few other creatures of the Plane of Fire, though few munsahirs honor her name, and a covert order of ifrits known as the Secret Fire is opposed to her rule. On Golarion, the Queen of the Inferno is worshipped primarily by fire wizards, arsonists, and dragons, especially cinder dragons.

**Title** Queen of the Inferno

**Areas of Concern** Fire, heat, smoke

**Edicts** Be passionate and quick of wit, destroy your foes with fire, inspire your inferiors with zeal and strategy

**Anathema** Allow yourself to stagnate or lose motivation, extinguish destructive blazes

**Religious Symbol** four flaming swords

**Sacred Animal** megalania

**Sacred Colors** orange, yellow

**Source:** `= this.source` (`= this.source-type`)
