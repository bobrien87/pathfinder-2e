---
type: deity
source-type: "Remaster"
domains: "Ambition, Confidence, Wyrmkin, Might"
favored-weapon: "Jaws, Spear"
divine-font: "Harm"
divine-skill: "Intimidation"
divine-spells: "Rank 1: [[Noxious Vapors]], Rank 3: [[Haste]], Rank 5: [[Impaling Spike]]"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

In the early days the skies were gray, for Garhaazh found his joy in billowing smoke throughout the cosmos. His was the role of a smoldering menace, a predator who dwelt within obscuring miasma, ever in search of a worthy competitor. The role of predator and of prey were nebulous at this time, but Garhaazh saw them made fundamental in the bitter strife between his brother Dahak and his father Apsu. He watched with glee from between shadowed stars as the pair fought unto the precipice of oblivion. It awoke something vicious and horrible in Garhaazh's bilious heart. Such violence did not cause him to hesitate or to fear, it made him hungry.

It was a joy unlike anything he'd ever known.

In crude emulation he replicated what he assumed was the source of conflict between his family. He claimed himself the Primal King, the First King, the ruler of all he could see—a feat made all the easier by his habit for shrouding existence in choking smoke. Cernunnos emerged from the dark of the cosmos, bow in hand, to strike down the Primal King who had enshrouded the stars. Garhaazh felt a sting of delight in his bones when he first looked upon his foe. But when the first arrow was flung, Garhaazh was aghast. He had expected a grapple, the gouging of claws, the ripping of teeth—but to throw a barb from a grand distance? That was new. He had not conceived that violence could involve unexpected things. In the eyes of Garhaazh, this made Cernunnos a deceiver and, as a deceiver, this meant that deception was now a fair tactic—a fundamental tactic—in the flow of conflict. Cernunnos would not be the last to enlighten the Primal King to new ways in which to enforce his reign of brutal bluster.

Though no nation can claim to center Garhaazh as their chief deity, he has served as the inspiration to countless tyrants and usurpers across history. His is the rhetoric of might making right, of self-important dominion, and of an ego that supplants the needs of the many in favor of short-term acts of carnage. In the modern era, he's firmly cast his gimlet eye upon Taldor. Since the start of Eutropia's reforms, the nationalist front of the Comolaudio Populi have rebuked her from the far-flung prefectures. Their sloganeering and protestations cloy for the return of a strongman leader. The Primal King offers boons to the most radical of these belligerents.

**Title** The Primal King

**Areas of Concern** conflict, dominance, hunting

**Edicts** act with mutual brutality, let might make right, always boast of your victories

**Anathema** act with humility, give mercy without supplication, die with grace

**Religious Symbol** crown of teeth, tusks, horns, or antlers

**Sacred Animal** none

**Sacred Colors** brass, gray, red

**Source:** `= this.source` (`= this.source-type`)
