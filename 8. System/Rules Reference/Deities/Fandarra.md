---
type: deity
source-type: "Remaster"
domains: "Death, Family, Knowledge, Nature"
favored-weapon: "Dagger"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Endure]], Rank 3: [[Wall Of Thorns]], Rank 5: [[Blister]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Fandarra (sometimes bearing the title of the Blood Mother, the Earth Mother, or Mother of All) is the giant god of blood, the cycle of life, knowledge, and fertility. Followers claim that all animals, all people, and all deities were born from her. Though most acts of piety in her name are performed by stone giants, many other types of giants, and even humans in cold climates like northern Avistan, worship her in some way, shape, or form as well. In largely giant followings, she is portrayed as a bald stone giant woman, her head adorned with a lush crown of leaves and flowers. Draped on her shoulders is a cloak of red fur, usually mammoth, bear, or wolf, and around her neck is a necklace of knives or arrowheads to bear against those who violate the natural cycles of life. When depicted in relation to fertility, she is also shown as pregnant, occasionally carrying an infant giant and bear in either arm. There are many tales of Fandarra in regard to her combat prowess, taking up arms to protect kin and the sanctity of life.

**Title** The Blood Mother

**Areas of Concern** Blood, the cycle of life, fertility, knowledge

**Edicts** Abide by the cycles of life, aid childbirth, destroy undead

**Anathema** Strive to break the cycle of life (such as by attaining immortality or creating undead), despoil the earth, kill a juvenile creature

**Religious Symbol** mountain and moon

**Sacred Animal** mammoth

**Sacred Colors** brown, ivory

**Source:** `= this.source` (`= this.source-type`)
