---
type: deity
source-type: "Remaster"
domains: "Fire, Healing, Protection, Sun"
favored-weapon: "Katar"
divine-font: "Heal"
divine-skill: "Performance"
divine-spells: "Rank 1: [[Soothe]], Rank 3: [[Ghostly Weapon]], Rank 4: [[Fire Shield]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Responsible for fire, purification, and radiance, Atreia the Lambent King is the benevolent elemental lord of fire. When the multiverse was young, Atreia soared across the Plane of Fire as a triple-headed ibis, with wings that burned and eyes of flame, routing evil from the plane. Though his strength was weakened from a long imprisonment, he maintained worship among some groups of munsahirs on the Plane of Fire for his dominion over protection and life-giving fire. With his return, his worship now also extends to a few circles of mortals who hold the discovery and purification of evil above all other causes.

**Title** The Lambent King

**Areas of Concern** Fire, purification, radiance

**Edicts** Burn away corruption, clear the way for new growth, purify tainted areas

**Anathema** Abandon a creature in darkness; deny a suffering creature warmth, shade, or water

**Religious Symbol** flaming wheel with six ibis wings

**Sacred Animal** ibis

**Sacred Colors** orange, white

**Source:** `= this.source` (`= this.source-type`)
