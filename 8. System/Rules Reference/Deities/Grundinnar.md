---
type: deity
source-type: "Remaster"
domains: "Confidence, Family, Protection, Truth"
favored-weapon: "Light-hammer"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Anticipate Peril]], Rank 4: [[Containment]], Rank 6: [[Wall Of Force]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Grundinnar is one of [[Torag]]'s many sons and is the dwarven god of friendship and loyalty. He is experienced at breaking up fights over his sister [[Bolka]], and has thus developed quite a strong sense of diplomacy. He uses this skill to end feuds, encourage neighborly conduct among his followers and works to ensure that dwarves remember friends they haven't seen in many years.

**Title** The Peacemaker

**Areas of Concern** Alliance, family, friendship, truth

**Edicts** Attempt to bridge the gap between feuding sides, maintain just treaties, maintain relations with neighbors

**Anathema** Sow discord among friends and allies, attack during parley

**Religious Symbol** pair of shaking hands

**Sacred Animal** horse

**Sacred Colors** gold, white

**Source:** `= this.source` (`= this.source-type`)
