---
type: deity
source-type: "Remaster"
domains: "Death, Might, Trickery, Zeal"
favored-weapon: "Sawtooth-saber"
divine-font: "Harm"
divine-skill: "Stealth"
divine-spells: "Rank 1: [[Sure Strike]], Rank 2: [[Invisibility]], Rank 4: [[Vision Of Death]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

While Achaekek's divine genesis is heavily debated among scholars, it is believed that he was created—either by the power of a singular deity or a group of them—to eradicate those who would steal a god's divinity. The creators are gone, perhaps by their creation's own claws. Achaekek remains, and he has since become the enforcer of divine punishment. Known as He Who Walks in Blood, he slumbers in the blood of heretics and worshippers alike. Sleeping in an immense cleft carved into the base of the Boneyard's spire, a realm known as the Blood Vale. He keeps no formal relationships with any other deities. Even his sister, Grandmother Spider, who repeatedly attempts to coax Achaekek to rebel against the gods and abandon his duties, barely warrants acknowledgment from the mantis god. In response, even though some gods disapprove of Achaekek's methods, few openly defy him. Rumors often fly about gods hiring Achaekek to assassinate another, but none of these claims have ever been proven.

**Title** He Who Walks in Blood

**Areas of Concern** assassins, divine punishment, the Red Mantis

**Edicts** conduct assassinations, spread the Red Mantis's infamy, wield sawtooth sabers in combat

**Anathema** kill a rightful ruler, become fixated on petty matters such as others' gender or ancestry, abandon an assassination contract you agreed to pursue

**Religious Symbol** crossed mantis claws

**Sacred Animal** crimson mantis

**Sacred Color** red

**Source:** `= this.source` (`= this.source-type`)
