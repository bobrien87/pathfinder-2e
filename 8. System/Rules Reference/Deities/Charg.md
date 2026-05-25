---
type: deity
source-type: "Remaster"
domains: "Abomination, Delirium, Might, Time"
favored-weapon: "Falchion"
divine-font: "Harm"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Sleep]], Rank 3: [[Hypnotize]], Rank 5: [[Stagnate Time]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

As it is the nature of mortals to destroy themselves, it is the nature of Charg to witness. The Typhon Wheel observes mortal catastrophes with keen interest and strict instruction to their followers to not interfere. Charg believes the decay of civilization and morals is a natural process and interference would be akin to the disruption of an unpolluted ecosystem.

**Title** The Typhon Wheel

**Areas of Concern** Catastrophic decline, detrimental complacency, monsters

**Edicts** Allow others to deal with their own mistakes, lead monsters to attack settlements, refrain from maintaining or fixing your possessions

**Anathema** Kill a monster that isn't a direct threat, meddle in situations that don't directly affect you

**Religious Symbol** monstrous eyes behind a crumbling wall

**Sacred Animal** sloth

**Sacred Colors** brown, rust red

**Source:** `= this.source` (`= this.source-type`)
