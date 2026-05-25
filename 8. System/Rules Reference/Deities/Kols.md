---
type: deity
source-type: "Remaster"
domains: "Knowledge, Might, Duty, Truth"
favored-weapon: "Light-hammer"
divine-font: "Harm, Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Phantasmal Minion]], Rank 4: [[Suggestion]], Rank 8: [[Unrelenting Observation]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

As Torag's firstborn, Kols was always a serious child. He watched how his father, chief among the dwarven gods, struggled to create deals and oaths that other deities would betray at their earliest convenience. He grew angry at the setbacks Torag had to endure from those who swore friendship but instead used him for their own selfish ends. Kols was baptized in the fires of being the eldest of Torag's children, a firsthand witness to his father's fury and pain. He thus vowed that he would do everything in his power to protect his father's followers, and also keep a record of those who had broken deals, broken faith, or shirked their duty in any way.

To many, Kols can seem a distant or angry god. While there is some truth to this, Kols is a devoted son and a courageous, protective brother. Grundinnar and Bolka speak of Kols highly, for even if he can be taciturn, they have seen love within him. Trudd often consults Kols about various interpretations of dwarven law, and they have conversations long into the night about what constitutes an oath versus what are empty boasts or simply words spoken in jest. These debates range from peaceful talks over tea to full-on drunken brawls, and Kols would have it no other way. Kols spends the most time with his father Torag, acting a barrister and diplomat to those who have sworn oaths in support of the Father of Creation, maintaining ties and always watching out for those whose faith could flag.

**Title** The Oathkeeper

**Areas of Concern** Duty, honor, promises

**Edicts** Seek those who break oaths and enforce just restitution, uphold your promises

**Anathema** Lie, dishonor yourself or your family, shirk your duties, break an oath

**Religious Symbol** rune-locked book

**Sacred Animal** lizard

**Sacred Colors** brown, green

**Source:** `= this.source` (`= this.source-type`)
