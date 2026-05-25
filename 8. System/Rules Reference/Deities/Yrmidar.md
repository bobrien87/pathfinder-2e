---
type: deity
source-type: "Remaster"
domains: "Family, Freedom, Indulgence, Moon"
favored-weapon: "Light-hammer"
divine-font: "Harm, Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Fleet Step]], Rank 2: [[Animal Form]], Rank 5: [[Moon Frenzy]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Yrmidar is a werebear frost giant deity of shipbuilders, camaraderie, and the hunt. When in his giant form, he is depicted as a frost giant with long silver hair in a braid that reaches past the small of his back, snowwhite eyes, and sharp obsidian-black fingernails. In his hybrid form, which is his most common form, his head transforms into that of a polar bear and his fingernails grow to become a bear's claws. In his werebear form, he becomes an enormous, bipedal polar bear with deadly fangs and claws. When he transforms into this beast, even the most battle-hardened of deities steer clear of him. Most mortals and gods alike consider this affliction a curse, but Yrmidar does not share that belief. To him and many of his followers, it is a power and a responsibility to be proud of and at peace with.

**Title** The Old Bear

**Areas of Concern** Camaraderie, the hunt, shipbuilders

**Edicts** Help your fellow neighbor, properly maintain ships and other sailing vessels you own, contribute to your community

**Anathema** Be too proud to give or ask for help, intentionally provoke wild animals, choose yourself over your community

**Religious Symbol** full moon with claw marks

**Sacred Animal** polar bear

**Sacred Colors** silver, white

**Source:** `= this.source` (`= this.source-type`)
