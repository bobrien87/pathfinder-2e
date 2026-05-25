---
type: deity
source-type: "Remaster"
domains: "Change, Creation, Nature, Perfection"
favored-weapon: "Claw, Fist"
divine-font: "Harm, Heal"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Lose The Path]], Rank 4: [[Vapor Form]], Rank 7: [[Possession]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Resembling nothing so much as the swirling, uncontrolled cacophony of planar potential that is the Maelstrom itself, Il'surrish the Wanderer is a formless, shapeless protean lord presiding over the untold infinities of unrealized potentials and possibilities. It celebrates the undefined and undecided, plans that linger unmade, power and discipline relinquished, and wild, unrestrained transformation. The Wanderer defies the pattern of chaotic philosophies championing the extremes of personal liberties and independence, teaching its followers to yield their avidity for control and instead allow the chaos inherent to the multiverse to guide them like a leaf gliding through a stream.

**Title** The Wanderer

**Areas of Concern** Formlessness, loss of control, potential

**Edicts** Achieve and revel in formlessness, surrender to uncertainty, take risks

**Anathema** Close off paths of action through slavish adherence to plans and commitments, become ruled by consequence

**Religious Symbol** cerulean sphere dotted with stars

**Sacred Animal** octopus

**Sacred Colors** cerulean

**Source:** `= this.source` (`= this.source-type`)
