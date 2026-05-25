---
type: deity
source-type: "Remaster"
domains: "Duty, Lightning, Pain, Protection"
favored-weapon: "Longsword"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Leaden Steps]], Rank 2: [[Enlarge]], Rank 6: [[Chain Lightning]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

In the pursuit of righteousness, one will suffer 10,000 little deaths. Those of purity will accept this torment and emerge knowing every danger the world might cast upon them, while those who flee like cowards from their task will know only their mortality. This truth was first claimed by Vineshvakhi, who even as a fledgling divinity couldn't begin to appreciate the gravity of his charge until he suffered pain and humiliation in its defense.

In ancient days, Vineshvakhi was tasked with protecting a blessed vault. Whatever it contained, Vineshvakhi knew only that he was to protect it, that he was never to look upon it, and that the asuras in all their blasphemous horror would seek to steal it. The raid by the asuras was a three-pronged attack. Vineshvakhi bested waves of fiendish horrors, resolute in his actions and unwilling to give an inch of ground or willpower to their corrupting devices. He turned the tide against Gavidya the Numberless's hordes, and struck true against Taraksun the Wakener of Wrath. The skies in Heaven were an erupting cacophony of brilliant lights, crashing blades, and fiendish miasma; in the end, it was Bohga who won the day. The Treasurer rana warped Vineshvakhi's own hand to remove the lock. Unwilling to cede any ground, the god of guardians severed each of his six fingers and spat in the eye of the rana.

Throughout the Impossible Lands, the ramifications of this conflict still carry forth. Calikangs were born from these divine fallen fingers and seek greater communion with the father they feel they failed when they were still part of his flesh. Ever resurgent, so too do asuras remain in dire numbers, pursuing the death of the divine. Wanderers of Vineshvakhi's order, the virajvinesh serve as sacred bodyguards, fiend hunters, and sacred slayers second only to the clerics of Abadar in their devotion to protection as a blessed concept.

**Title** The Pain of Purity

**Areas of Concern** Guardians, locks, sacrifice, vaults

**Edicts** Protect holy people, places, and treasures; sacrifice common comforts and mortal joys for the sake of your charge

**Anathema** Abandon your post, fail to protect your charge, willingly suffer corruption over death or grievous harm

**Religious Symbol** trident with a lock in its head

**Sacred Animal** buffalo

**Sacred Colors** purple, gold

**Source:** `= this.source` (`= this.source-type`)
