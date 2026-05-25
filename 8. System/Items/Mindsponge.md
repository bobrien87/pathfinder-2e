---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Mental]]", "[[Occult]]"]
price: "{'gp': 700}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

A *mindsponge* appears as a misshapen gray sponge that unsettlingly resembles a malformed human brain. Though pliable in all the same ways as a damp sponge, a *mindsponge* has no ability to absorb water and, in fact, doesn't seem terribly porous at all. Instead, a *mindsponge* is used to absorb thoughts and memories from living creatures.

**Activate—Wipe Memories** `pf2:2` (concentrate, manipulate)

**Effect** The *mindsponge* casts [[Rewrite Memory]], but only to erase a memory—a *mindsponge* can't enhance memory clarity, alter memories, or add false memories.

**Activate—Absorb Memories** 1 minute (concentrate, manipulate)

**Effect** You use the *mindsponge* to harvest the memories and mental energy of a specially prepared target as it dies. To prepare the target (who must be willing or helpless), you must perform a 10-minute surgery to expose a portion of the target's brain without killing them. This requires a successful DC 28 [[Medicine]] check (master) check; if you fail this check, the target dies before you can use the *mindsponge*.

Memories and psychic energy absorbed aren't taken from the target's soul but from energies temporarily infused within the body, so that a creature slain in this way who is later brought back to life retains their harvested memories and energy. The corpse of someone who has had their memories harvested is difficult to communicate with via talking corpse—treat the saving throw result against that spell as one degree of success lower than the actual result.

A *mindsponge* can store the memories and energy of up to four creatures at a time. Once full, it cannot be activated at all, other than to squeeze it as an Interact action with the concentrate trait, which causes all of the memories within to drip out as cold ectoplasm, which swiftly evaporates if not used or contained.

**Source:** `= this.source` (`= this.source-type`)
