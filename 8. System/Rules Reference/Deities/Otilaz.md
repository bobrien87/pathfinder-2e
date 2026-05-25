---
type: deity
source-type: "Remaster"
domains: "Change, Death, Introspection, Soul"
favored-weapon: "Jaws, Mace"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Phantom Pain]], Rank 3: [[Curse Of Lost Time]], Rank 8: [[Canticle Of Everlasting Grief]]"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

The One of All was never born and thus will forever be untarnished by the fallibility that any existence would inevitably bring. It's held eternally in the memory of Sarshallatu as the purest of her clutch, as the one who would have graced creation and brought meaning to all that could be seen. The name she had chosen for the ill-fated soul that Dahak brought crashing down upon the head of Apsu was to be Otilaz. And Otilaz was to be perfect.

In the fickle nature of the ineffable, Otilaz was not born—yet Otilaz does exist. Its quintessence stirred despite its material form being brutalized and cast limp upon the horrified visage of Apsu. It watched as Dahak gnawed upon one of its errant limbs and spat cursed words in a language that rattled the firmament and pulled fraying threads upon the Dark Tapestry. Otilaz looked upon its corpse, and it felt enlightened.

It knew it was meant to exist. It knew its material form held meaning; it invoked horror in a father, sorrow in a mother, and that it was known to be catalyst for both to its sibling. It wondered why such eternal powers could feel this way toward something that never was, and in contemplation of this truth it glimpsed enlightenment upon the nature of impermanence.

**Title** The One Of All

**Areas of Concern** alchemy, death, impermanence

**Edicts** learn from observed mistakes, promote change and growth, accept the inevitable

**Anathema** seek immortality or enlightenment, become stagnant, believe yourself a learned master

**Religious Symbol** alchemical symbol of the ouroboros

**Sacred Animal** amphisbaena

**Sacred Colors** black, blue, red, white

**Source:** `= this.source` (`= this.source-type`)
