---
type: deity
source-type: "Remaster"
domains: "Glyph, Knowledge, Secrecy, Undeath"
favored-weapon: "Morningstar"
divine-font: "Harm"
divine-skill: "Survival"
divine-spells: "Rank 1: [[Message Rune]], Rank 2: [[Feast Of Ashes]], Rank 5: [[False Vision]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Said to have begun his existence as a lowly cacodaemon, Pavnuri gained power by consuming others of his kind and by buying and selling secrets throughout Abaddon. As a harbinger, he is the plane's foremost information broker. Though he has served each of the Riders of the Apocalypse over the centuries, he has betrayed them all at one point or another. Despite that, Pavnuri still claims that they respect him. Many of his contacts and worshippers are cannibalistic undead to whom he feeds mere morsels of the knowledge that might answer the mysteries of the planes, never revealing the full truth. Pavnuri preys on those who so desperately chase secrets—the weakness of seemingly indomitable foe, the rumor that might undo a rival, the academic epiphany that will secure immortality—that they neglect their necessary mortal functions, such as eating.

**Title** The Lord of Nothing

**Areas of Concern** Cannibalism, secret messages, starvation

**Edicts** Consume the flesh of your own kind, hoard secrets, never speak plainly when you can speak in metaphor or code

**Anathema** Feed another out of kindness or pity, give up an intimate secret without gain

**Religious Symbol** maw and fiery pyramid

**Sacred Animal** ape

**Sacred Colors** black

**Source:** `= this.source` (`= this.source-type`)
