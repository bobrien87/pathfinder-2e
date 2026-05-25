---
type: deity
source-type: "Remaster"
domains: "Family, Nature, Protection, Travel"
favored-weapon: "Staff"
divine-font: "Heal"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Summon Animal]], Rank 2: [[Speak With Animals]], Rank 5: [[Animal Form]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Within the Realm of the Mammoth Lords, animals often hold as much importance as people, for both have spirits and are a part of the natural world. Most followings consider animals equal members of the community and treat these beings with respect. Of all the spirits and gods of animals, most people of the Realm feel kinship with Rowdrosh. The empyreal lord Rowdrosh is to animals what Bergelmir is to people—a guide and caretaker who binds members of a community together with common goals and feelings of kinship. It was Rowdrosh who convinced the first animals to join in groups bound not just by survival, but by companionship. Rowdrosh lived among the packs and herds, eventually settling among a herd of sheep and partially adopting their form. He was the first to domesticate an animal, and with patience and his blessing, countless people have followed in his footsteps since, taming dogs, oxen, sheep, mammoths, and far wilder creatures throughout the ages. Rowdrosh teaches people to watch over those in their charge—whether a literal herd or members of a following—and to treat animals with the kindness, care, and patience they would afford their own kin. Rowdrosh's influence in shaping the modern following is undeniable, even among those groups that don't pay homage to him.

Rowdrosh is a shapeshifter capable of transforming into countless animal forms, but artistic depictions of the Herdsman are surprisingly consistent. He's shown as a strong Kellid man with brown skin and thick black hair covering his head, chest, and shoulders. His head sports two curving horns made of moonstone, and he wields a wooden crook. Rowdrosh supposedly travels the lands in the guise of a herd animal from time to time, to test the care that each following offers to their animal members.

**Title** The Herdsman

**Areas of Concern** Animal husbandry, herd animals, shepherds

**Edicts** Aid your community, protect those you have authority over, treat animals with respect

**Anathema** Abandon your community, neglect those in your care, torment animals

**Religious Symbol** Double-headed crook

**Sacred Animal** Sheep

**Sacred Colors** green, ivory

**Source:** `= this.source` (`= this.source-type`)
