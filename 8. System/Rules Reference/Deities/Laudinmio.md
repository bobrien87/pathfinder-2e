---
type: deity
source-type: "Remaster"
domains: "Change, Creation, Metal"
favored-weapon: "Alchemical-bomb"
divine-font: "Harm, Heal"
divine-skill: "Crafting"
divine-spells: "Rank 1: [[Fold Metal]], Rank 2: [[Summon Elemental]], Rank 5: [[Impaling Spike]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Laudinmio, the Sovereign of Alchemy, is the elemental lord of metal, alchemy, and experimentation. They once thrived on the quicksilver change of minerals and metals when correctly combined, seeking the most innovative of crafts, chemical reactions, and fashion. Incursions from Ayrzul have left Laudinmio in a tragic state, trapped in a nightmarish slumber, their short bouts of lucidity haunted by regret and confusion. Their realm on the Plane of Metal, known as the Euphonious Coalition, still houses their loyal subjects, who seek for means to ease Laudinmio's torment.

**Title** The Sovereign of Alchemy

**Areas of Concern** Alchemy, discovery, experiments, metal, regret

**Edicts** Discover new alloys and concoctions, have multiple concurrent plans, innovate use of metals

**Anathema** Allow your creation to fall into malicious hands, destroy an alchemical formula

**Religious Symbol** sigil made of precious metals

**Sacred Animal** scaly-foot snail

**Sacred Colors** copper, silver

**Source:** `= this.source` (`= this.source-type`)
