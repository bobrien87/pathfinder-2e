---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Fire]]", "[[Magical]]"]
price: "{'gp': 4200}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This exquisite, shimmering rhyton is made from volcanic glass and encrusted with rubies, garnets, and other red gemstones, with a blown glass sculpture of a snakelike fire elemental at its base. It was sculpted as part of a 10-piece set of drinking horns, created to match a powerful ifrit shuyookh's entertaining dinnerware, but it became separated from the rest of the collection. Whether for good or ill, the beautiful glass rhyton still carries tidings from its previous shuyookh owner, and you become their esteemed guest from afar whenever you hold it.

The drinking horn functions as a [[Bottomless Stein]], refilling with a common ale each time it's emptied. However, anyone holding the rhyton who whispers the name of its former shuyookh owner has the horn filled with their favorite wine, spirit, juice, or other beverage from anywhere across the many planes, as if their wish were granted by a magnanimous genie.

**Activate—Toast!** `pf2:1` (manipulate)

**Effect** You raise a toast to a creature or creatures you're about to socialize with. You gain a +2 item bonus to Deception, Diplomacy, or Intimidation checks against those creatures for 1 hour.

**Activate—Ifrit's Command** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** An ifrit's hospitality always comes with an implied threat. You cause the shuyookh to briefly appear and take its vengeance on those who would hurt you, the genie's "guest." The shuyookh issues a 6th-rank [[Command]] that targets all creatures hostile to you in range instead of the usual number of targets. The shuyookh issues the same command to all of them. Each target that fails its save also feels all nourishment leached from it, becoming [[Fatigued]] as long as it's affected by the command.

**Source:** `= this.source` (`= this.source-type`)
