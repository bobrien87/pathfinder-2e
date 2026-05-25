---
type: deity
source-type: "Remaster"
domains: "Decay, Pain, Plague, Undeath"
favored-weapon: "Dart"
divine-font: "Harm"
divine-skill: "Medicine"
divine-spells: "Rank 1: [[Goblin Pox]], Rank 2: [[Vomit Swarm]], Rank 7: [[Corrosive Body]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Sometimes, desperate individuals suffering in the wake of plague and illness cry out to the cosmos for aid. Xsistaid is the chittering voice attempting to convince them that their continuing survival means shedding all pretenses of goodness, and preying upon whomever is in reach, growing strong by robbing others of their vitality. The Wriggling Wound cares not that there is no honor in becoming a parasite. Only the fact that it leads to a longer life matters.

**Title** The Wriggling Wound

**Areas of Concern** Festering injuries, maggots, parasites

**Edicts** Feed on others without guilt, rob others of strength to embolden yourself, wield your weakness as your weapon

**Anathema** Fail to take advantage of someone's kindness, take only what you need when you could get away with more

**Religious Symbol** mouthful of maggots

**Sacred Animal** botfly

**Sacred Colors** brown, white

**Source:** `= this.source` (`= this.source-type`)
