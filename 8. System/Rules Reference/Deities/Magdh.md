---
type: deity
source-type: "Remaster"
domains: "Fate, Glyph, Knowledge, Truth"
favored-weapon: "Scythe"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Anticipate Peril]], Rank 3: [[Threefold Aspect]], Rank 6: [[Scrying]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Magdh is the Eldest of foreknowledge, complexity, and triplets, and she is the greatest seer in the First World. Most often appearing as a woman with three faces set equidistantly around her head, Magdh looks across the skeins of fate into myriad alternate realities and possible futures. Among all the Eldest, she has the deepest knowledge of reality's true design and the ripples a single action or inaction can create throughout all of existence. Her communications are veiled in conditional language and oddly juxtaposed statements to an almost infuriating degree, and thus she never communicates the prophetic truths she sees—so plain to her six eyes—in a straightforward way. Because of their shared knowledge of branching timelines, Shyka and Magdh can communicate more easily with each other about such topics, though the other Eldest are cautious around Magdh, lest a careless comment or errant gesture cause her to predict apocalyptic dooms.

**Title** The Three

**Areas of Concern** Complexity, fate, triplets

**Edicts** Use magic to read the future and understand fate

**Anathema** Lie, share your magic readings without payment (no matter how trivial)

**Religious Symbol** green three-pointed knot

**Sacred Animal** multi-headed animals

**Sacred Colors** blue, green

**Source:** `= this.source` (`= this.source-type`)
