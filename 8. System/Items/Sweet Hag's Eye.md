---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Occult]]", "[[Scrying]]"]
price: "{'gp': 75}"
usage: "worn"
bulk: "—"
source: "Pathfinder Adventures: Troubles in Grayce"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This item appears to be a normal, if admittedly macabre, piece of hard peppermint candy the size and shape of a human eyeball. That's because it is actually the eye of a sweet hag, removed and painstakingly replaced with a mix of enchantment and cookery. It is typically mounted on a piece of jewelry or stored in a small sack worn on a cord.

The eye provides no direct benefit for the wearer, but the hag whose eye it once was can peer through it using the `act seek` action, and cast the [[Message]] cantrip through it onto the creature carrying the eye. Both these effects have no range limited, provided the hag is on the same plane.

Any damage to the eye destroys it. The sweet hag can also choose to destroy the eye remotely using Meltaway Mint. The eye can also be eaten, but a creature who attempts this is exposed to sickeningly sweet.

**Activate—Meltaway Mint** `pf2:1`

**Effect** The hag causes the eye to melt away under a brief flare of intense heat. If a creature is holding the eye, they must attempt a DC 18 [[Reflex]] save. On a failure, they take 1d4 persistent,fire damage as the boiling hot candy remains stick to and burn their skin.

**Sickeningly Sweet** (ingested, poison) The sickened condition caused by this poison can't be ended until the poison's effects end

**Saving Throw** DC 20 [[Fortitude]] save

**Onset** 1 minute

**Maximum Duration** 10 minutes;

**Stage 1** [[Sickened]] 1 (1 minute)

**Stage 2** 1d8 poison damage and [[Sickened]] 2 (1 minute)

**Stage 3** 2d8 poison damage and [[Sickened]] 3 (1 minute)

**Craft Requirements** You must be a sweet hag.

**Source:** `= this.source` (`= this.source-type`)
