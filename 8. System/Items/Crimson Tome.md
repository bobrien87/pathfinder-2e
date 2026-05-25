---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Grimoire]]", "[[Illusion]]"]
price: "{'gp': 15000}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These tomes are sacred to the Red Mantis assassins, who use them to scribe their spells and record their violent deeds. The first of them were created in Rahadoum, but when the Oath Wars forced the worshippers of Achaekek to flee Rahadoum, many were identified by their *crimson tomes*, which were destroyed on the spot. Less than a dozen volumes survived, and the secret of creating them has been lost to history. Rumors persist of a first edition of this rare tome—an artifact version of the one presented here, but if these rumors are true, even the Red Mantis have lost track of such a treasure.

Each *crimson tome* is bound in fine red leather with gold filigree on the cover and golden edge gilding. When an illusion spell is prepared from this grimoire, it becomes more difficult to purposefully disbelieve. Creatures that attempt to disbelieve an illusion spell prepared from a *crimson tome* must roll their check twice and take the worse result; this is a misfortune effect. This does not affect the saving throws of spells with the illusion trait that call for a saving throw to resolve effects other than disbelief, such as with [[Dizzying Colors]] or [[Vision of Death]].

**Activate—Crimson Focusing** `pf2:1` (manipulate)

**Frequency** once per day

**Requirements** You have fewer Focus Points than your maximum number of Focus Points

**Effect** You draw on the *crimson tome's* energies and regain one Focus Point; the *crimson tome's* leather binding turns black until your next daily preparations.

**Activate—Achaekek's Gift** `pf2:r` (concentrate, spellshape)

**Trigger** You kill a creature with a spell prepared from the *crimson tome*

**Effect** The *crimson tome* infuses the slain creature's mortal remains and soul. If an effect attempts to restore the slain creature to life, the *crimson tome* immediately attempts to counteract that effect (counteract modifier +27, counteract rank 8). If the restoring effect is counteracted, you immediately learn the name, nature, and location of the creature or effect that attempted to bring the dead body back to life. You can only impart Achaekek's Gift on one creature at a time. If you use this ability on another creature, the previous creature loses Achaekek's Gift.

**Source:** `= this.source` (`= this.source-type`)
