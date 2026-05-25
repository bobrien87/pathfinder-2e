---
type: deity
source-type: "Remaster"
domains: "Fire, Knowledge, Nature, Travel"
favored-weapon: "Dogslicer"
divine-font: "Harm"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Vanishing Tracks]], Rank 3: [[Fireball]], Rank 7: [[Unfettered Pack]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Zarongel is the creator-god of dog killing, fire, and mounted combat. That barghests are profoundly dogshaped seems not to matter to either Zarongel or his followers. By all accounts, Zarongel appears to despise domesticated canines for becoming subservient to mortals. He's often depicted as a wolf-like barghest with his hair composed of burning fire. His mouth drips a magma-like substance that mimics molten saliva.

**Title** The Bark Breaker

**Areas of Concern** Arson, hunt, ritual

**Edicts** Learn mounted combat, perform arson, hunt and kill dogs

**Anathema** Befriend or spare a dog

**Religious Symbol** severed dog's paw

**Sacred Animal** goblin dog

**Sacred Colors** orange, yellow

**Source:** `= this.source` (`= this.source-type`)
