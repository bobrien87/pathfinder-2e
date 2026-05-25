---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Apex]]", "[[Artifact]]", "[[Intelligent]]", "[[Invested]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder #212: A Voice in the Blight"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +33; precise low-light vision and hearing within 30 feet

**Communication** telepathy (partner only)

**Skills** Arcana +35, Architecture Lore +35, Society +35

**Int** +7, **Wis** +5, **Cha** +6

**Will** +33

The stoic echo of Candlaron the Sculptor, architect of the aiudara network, infuses the *Guiding Star Orb*. As long as you have him invested, the *Guiding Star Orb* orbits your body instead of needing to be held in one hand. You can stow the *Guiding Star Orb* with an Interact action, and he can be snatched out of the air with a successful [[Disarm]] action against you. When stowed, the *Guiding Star Orb* remains invested, but if he's removed from you via Disarm, your investment ends if you don't reclaim him by the end of your next turn. The *Guiding Star Orb's* voice is scholarly and precise, speaking telepathically with clearly enunciated but often complex words, and he assumes you're educated enough to keep up with his academic dialogue.

As long as you have the *Guiding Star Orb* invested, teleportation effects created by you or the *Guiding Star Orb* aren't affected by the Witchbole's meddling with teleportation effects, and they can't be counteracted by the Witchbole.

**Activate—Blinding Spark** `pf2:2` (concentrate, incapacitation, light, visual)

**Effect** The *Guiding Star Orb* creates a beam of bright light and fires it at a creature within 30 feet. That creature must attempt a DC 43 [[Fortitude]] save, after which that creature is temporarily immune to Blinding Spark for 24 hours.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Dazzled]] for 1 round.
- **Failure** The target is [[Blinded]] for 1 round.
- **Critical Failure** The target is permanently blinded.

**Activate—Embed Location** `pf2:2` (concentrate)

**Effect** By focusing, the *Guiding Star Orb* embeds your current location within. Thereafter, anyone who touches the *Guiding Star Orb* while casting a spell with the teleportation trait to travel to this location arrives precisely, without any inaccuracy at all. The *Guiding Star Orb* can have up to three locations embedded at a time; if this activity is used a fourth time, the new location replaces the oldest stored one.

**Activate—Momentary Aiudara** 10 minutes (concentrate)

**Frequency** once per day

**Effect** A shimmering magical archway appears next to you as the *Guiding Star Orb* casts a 9th-rank [[Teleport]] to your specifications. If you're teleporting to an aiudara you've visited before, you and the targets appear precisely at that location. If you're teleporting to Lotusgate in Kyonin, this effect functions as [[Interplanar Teleport]] if you aren't on the same plane as Kyonin.

**Source:** `= this.source` (`= this.source-type`)
