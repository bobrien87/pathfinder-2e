---
type: deity
source-type: "Remaster"
domains: "Darkness, Moon, Nature, Secrecy"
favored-weapon: "Longbow"
divine-font: "Harm, Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Vanishing Tracks]], Rank 2: [[Invisibility]], Rank 3: [[Animal Vision]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Ketephys is the tight-lipped elven god of the hunt, who instructs his followers to care for the forest and defend it from his arch-enemy [[Treerazer]].

**Title** The Hunter

**Areas of Concern** Forestry, hunting, running, the moon

**Edicts** Hunt and kill demons and undead, maintain the health of the forest, provide for your community

**Anathema** Take more than needed from the wilderness, hunt an animal for sport, aid Treerazer or his minions

**Religious Symbol** hawk with moon and sun

**Sacred Animal** hawk

**Sacred Colors** gold, silver

**Source:** `= this.source` (`= this.source-type`)
