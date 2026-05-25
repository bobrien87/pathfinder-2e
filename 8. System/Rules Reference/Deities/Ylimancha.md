---
type: deity
source-type: "Remaster"
domains: "Air, Nature, Travel, Water"
favored-weapon: "Longbow"
divine-font: "Harm, Heal"
divine-skill: "Acrobatics"
divine-spells: "Rank 1: [[Gentle Landing]], Rank 3: [[Feet To Fins]], Rank 4: [[Aerial Form]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Ylimancha gazes out over the world's coastlines, presiding over coastal waters, fishers, and flying creatures. Also known as Harborwing, she believes in harmony between the seas, the skies, and the beings of the land. Sustenance and resources can be taken from the sea by those on shore, but not so much that the balance is upset. The sea may sometimes encroach on the land, but breakwaters can be built to keep communities on land dry and safe. Ylimancha likewise loves all creatures that fly, though the demon lord Pazuzu also claims dominion over them, bringing the two into endless conflict and causing her to mourn deeply each creature he converts to his worship.

**Title** Harborwing

**Areas of Concern** Coastal waters, fishers, flying creatures

**Edicts** Teach sustainable fishing, swim in saltwater, fly

**Anathema** Imprison birds or clip their wings, poison coastal waters, overfish, aid Pazuzu or his minions

**Religious Symbol** golden seagull

**Sacred Animal** seagull

**Sacred Colors** blue, gold

**Source:** `= this.source` (`= this.source-type`)
