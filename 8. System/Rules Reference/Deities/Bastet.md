---
type: deity
source-type: "Remaster"
domains: "Nature, Passion, Protection, Trickery"
favored-weapon: "Claw, Tekko-kagi"
divine-font: "Heal"
divine-skill: "Deception"
divine-spells: "Rank 1: [[Pest Form]], Rank 3: [[Animal Vision]], Rank 4: [[Peaceful Bubble]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Bastet is the patron of rogues and bards. She is particularly popular among women, and most of her clerics are female. They usually keep cats as pets, and when these cats die, they are mummified and buried with their owners.

**Title** The Sly Enchantress

**Areas of Concern** Cats, pleasure, secrets

**Edicts** Learn secrets, tempt others into revelry, kill harmful snakes and evil spirits, heal diseases

**Anathema** Kill or abuse a house cat, abandon a child, choose to marry

**Religious Symbol** golden cat

**Sacred Animal** cat

**Sacred Colors** russet, gold

**Source:** `= this.source` (`= this.source-type`)
