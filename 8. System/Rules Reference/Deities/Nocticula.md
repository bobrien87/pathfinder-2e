---
type: deity
source-type: "Remaster"
domains: "Change, Creation, Darkness, Travel"
favored-weapon: "Dagger"
divine-font: "Heal"
divine-skill: "Society"
divine-spells: "Rank 1: [[Penumbral Shroud]], Rank 3: [[Veil Of Privacy]], Rank 4: [[Creation]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

For most of her existence, Nocticula was a patron of assassins and succubi, a demon lord feared by other demon lords for her skill at assassinating the competition. Those days are behind Nocticula, for she has risen to the role of the Redeemer Queen, a patron of marginalized artists and protector of those cast out from society. She is now feared among her former peers for her persuasive words that tempt them away from their place in the Outer Rifts and toward redemption. Her faith is strongest in the eastern reaches of New Thassilon, where her most powerful exile, Queen Sorshen, seeks to build a nation that welcomes those whom others have cast out. She is also popular among the Alijae elves of the Mwangi Expanse, who were among the first to notice her ascension.

Unlike deities such as Sarenrae and Shelyn, Nocticula's concept of redemption tends to be a personal matter. She has little interest in demanding atonement and recompense for past wrongs, assuming such a feat is even possible—her own history is soaked in blood and far more vicious violations, with sins committed that can never be undone. The Redeemer Queen instead encourages evildoers to step away from the hells of their own making, to put aside their ways and stop causing harm rather than to remain trapped in their vicious cycles of violence. Though gods of justice might rankle at the concept, Nocticula's philosophy attracts many who might not be swayed otherwise. Few fiends have any interest in putting in the hard work to make up for their crimes, but many tire of the unending viciousness and cruelty of their peers. Nocticula provides a tempting solace, and every now and then an odd demon slips away to make their way to her realm.

**Title** The Redeemer Queen

**Areas of Concern** artists, exiles, midnight

**Edicts** create art true to yourself, protect marginalized artists, punish those who take advantage of offered trust and shelter

**Anathema** deny shelter to the desperate, destroy harmless art you dislike, finish a work of art during daylight hours

**Religious Symbol** moon with smirking lips and a seven-pointed crown

**Sacred Animal** bat

**Sacred Color** blue, purple

**Source:** `= this.source` (`= this.source-type`)
