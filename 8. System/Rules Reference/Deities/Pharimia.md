---
type: deity
source-type: "Remaster"
domains: "Duty, Fire, Travel, Water"
favored-weapon: "Ranseur"
divine-font: "Heal"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Tailwind]], Rank 2: [[Floating Flame]], Rank 5: [[Control Water]]"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

For a divinity of clarity and light, Pharimia's origins are ironically murky; she has traveled the archipelago to build lighthouses, signal fires, and ports throughout living memory. She asks for little in return beyond respect for travelers and responsible infrastructure budgeting to maintain what she creates. In any other age, her mundane mission would be forgettable. However, as myth-speaking became unreliable and the pantheon dwindled, Pharimia has become a self-appointed defender of Iblydan hero-gods and their associated traditions. She's one of the few voices that can convince unholy demigods and righteous divinities to unite against common threats. Her priests seek similar challenges, serving as negotiators and leaders for ragtag coalitions whose members would otherwise stab each other in the back.

**Title** The Horizon Flame

**Areas of Concern** ports and lighthouses

**Edicts** guide others between places of safety, maintain travel infrastructure, unite contentious parties to achieve greater goals

**Anathema** deny directions to the lost, extinguish a lighthouse or similar beacon, bring destruction upon Iblydos

**Religious Symbol** three stars above a lighthouse

**Sacred Animal** rattlesnake

**Sacred Colors** red, yellow

**Source:** `= this.source` (`= this.source-type`)
