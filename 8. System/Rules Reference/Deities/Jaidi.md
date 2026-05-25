---
type: deity
source-type: "Remaster"
domains: "Family, Might, Nature, Sun"
favored-weapon: "Scythe"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Protector Tree]], Rank 3: [[Wall Of Thorns]], Rank 5: [[Nature'S Pathway]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Jaidi, the Blessing and Bounty, was the Azlanti goddess of agriculture, hard work, and self-sufficiency. While primarily worshipped during the era of ancient Azlant society, artifacts dedicated to her were found in ancient ruins by Azlanti explorers, suggesting her existence for millennia prior. Most of her history and story of origin remains a mystery.

What is known is that Jaidi is the spouse of another god, Erastil. The beginnings of their relationship are a matter of much speculation. Some say the two met during the Age of Creation, battling side by side against Rovagug, starting an epic romance forged in the fires of battle. Others say the two agreed on a mutually beneficial arrangement to strengthen both churches' beliefs in hard work and community to aid fledgling human society. Still more speak of a time that Erastil was a wild beast, lured in by Jaidi's agriculture and tamed by her love.

**Title** The Blessing and Bounty

**Areas of Concern** Agriculture, hard work, self-sufficiency

**Edicts** Encourage hard work that benefits all, ensure the health of crops and vegetation, always lend a hand when asked

**Anathema** Destroy healthy crops, waste food, refuse to help others in your community

**Religious Symbol** shepherd's crook bearing a sun

**Sacred Animal** horse

**Sacred Colors** olive green

**Source:** `= this.source` (`= this.source-type`)
