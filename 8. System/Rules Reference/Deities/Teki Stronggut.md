---
type: deity
source-type: "Remaster"
domains: "Family, Freedom, Might, Protection"
favored-weapon: "Longsword"
divine-font: "Harm, Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Tailwind]], Rank 2: [[Embed Message]], Rank 7: [[Retrocognition]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Teki Stronggut surprised many scholars in Golarion when she suddenly ascended as a hero-god; most had never heard of her or knew only stories of her failures. Those who personally knew her, however, describe Teki as the kind of person who always ends up achieving her dreams, despite many setbacks and the obvious odds. Goblins, bugbears, and all kinds of unlikely adventurers were rooting for her, as she remembered and represented them all. "Everyone can become a hero if they put their mind to it," or so Teki would put it. Teki appears much like she did in life: a goblin with bright yellow skin, a cloak with images of failed heroes she supported in her life, a variety of old weapons and other adventuring junk, and an unremovable grin.

**Title** The Rememberer

**Areas of Concern** Haplessness, heroism, the forgotten

**Edicts** Remember those whom others forget, help those who need it the most, aid other misfits in their goals

**Anathema** Give up on your cause, punish someone due to failure or incompetence, abandon a fellow adventurer

**Religious Symbol** sword on a pedestal

**Sacred Animal** mouse

**Sacred Colors** pink, gold

**Source:** `= this.source` (`= this.source-type`)
