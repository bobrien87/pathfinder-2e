---
type: deity
source-type: "Remaster"
domains: "Family, Knowledge, Protection, Sorrow"
favored-weapon: "Staff"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Gentle Landing]], Rank 4: [[Aerial Form]], Rank 6: [[Collective Transposition]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Called Grandmother Crow, Andoletta represents consolation, respect, and security. Andoletta makes a clear distinction between guilt and innocence: there is no in-between. For those falsely accused or who show signs of redemption, she offers a path back to the light. That path is never an easy one, but it is one worth walking, and she stands beside those who make the trek. For the truly wicked and those who show no remorse, she has no mercy. For these reasons, her likeness is often found in courts, where she can watch over and ensure fairness to those accused of crimes. Andoletta also places great value on respect for the dead and the protection of children. To offer solace to the bereaved is true kindness and compassion. Children are slates with tremendous potential for good-if they can be guided and kept safe from evil.

**Title** Grandmother Crow

**Areas of Concern** Consolation, respect, security

**Edicts** Respect elders, instill good virtues in children, seek and allow redemption

**Anathema** Hold a grudge, mock the dead, pass judgment hastily or carelessly

**Religious Symbol** hand with willow staff

**Sacred Animal** crow

**Sacred Colors** black, green

**Source:** `= this.source` (`= this.source-type`)
