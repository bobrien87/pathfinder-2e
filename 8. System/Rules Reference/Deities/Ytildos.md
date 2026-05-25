---
type: deity
source-type: "Remaster"
domains: "Delirium, Secrecy, Water, Wealth"
favored-weapon: "Macuahuitl"
divine-font: "Harm"
divine-skill: "Thievery"
divine-spells: "Rank 1: [[Hydraulic Push]], Rank 3: [[Coral Scourge]], Rank 8: [[Whirlpool]]"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

In her efforts to kill other hero-gods, Ongalte performed an act of hypocrisy: she created a hero-god of her own. A marauder and iconoclast, the pirate Ytildos seemed like a perfect lieutenant who could hound Iblydos's pantheon from the sea. However, when Pharimia wounded Ongalte in battle, the cyclops fled and relied on Ytildos to guard her as she recuperated. He did… for a time. Greed and contrariness got the better of him, and he absconded with much of Ongalte's wealth, earning her eternal ire.

Ytildos is an inconsistent divinity. One moment, he's encouraging his worshippers to cause and pilfer shipwrecks, only to become jealous of their newfound wealth. It's common for sailors to cast a portion of their wealth into the sea, hoping to assuage the hero-god's avarice. He drags the ships of any who fail to placate him onto reefs, delighting as the coral tears open a vessel's belly and spills its cargo into the sea.

**Title** The Tidefang

**Areas of Concern** reefs and shipwrecks

**Edicts** capitalize on others' misfortune for profit, subtly ruin navigation tools, set traps

**Anathema** despoil a coastal ecosystem, give away a treasure map for free

**Religious Symbol** a ship wrecked atop a reef

**Sacred Animal** hermit crab

**Sacred Colors** brown, orange

**Source:** `= this.source` (`= this.source-type`)
