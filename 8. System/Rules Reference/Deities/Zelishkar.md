---
type: deity
source-type: "Remaster"
domains: "Destruction, Duty, Fire, Zeal"
favored-weapon: "Ranseur"
divine-font: "Harm"
divine-skill: "Acrobatics"
divine-spells: "Rank 1: [[Breathe Fire]], Rank 4: [[Fire Shield]], Rank 7: [[Fiery Body]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The Bitter Flame was originally forged by Szuriel, the Rider of War, in her domain, the Cinder Furnace. She created Zelishkar as the embodiment of the funeral pyres that often follow in the wake of the wars she brings. The aggressive daemonic feline performed his duties so well that Szuriel promoted him to harbinger. Though Zelishkar continues to personify the most sadistic uses of fire, he holds a spark of resentment in his cores that he owes all that he is to Szuriel and schemes to someday supplant her.

**Title** The Bitter Flame

**Areas of Concern** Arson, burning alive, cremation

**Edicts** Burn the remains of your defeated enemies and closest allies, destroy the accomplishments of your so-called betters, wield flame as a tool and a weapon

**Anathema** Accept the motivations of others at face value, extinguish a raging fire

**Religious Symbol** crossed pikes over a pyre

**Sacred Animal** tiger

**Sacred Colors** orange, red

**Source:** `= this.source` (`= this.source-type`)
