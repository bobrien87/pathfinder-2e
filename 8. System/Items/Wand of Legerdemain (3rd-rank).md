---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]", "[[Wand]]"]
price: "{'gp': 500}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This wand of lacquered black wood has a handle wrapped in interwoven colorful ribbons. A silver bell caps the wand's tasseled pommel.

**Activate** Cast a Spell

**Frequency** once per day, plus overcharge

**Effect** You Cast the Spell.

**Activate** `pf2:1` (emotion, illusion, light, manipulate. mental, visual)

**Requirements** The last action you took this turn was to Cast a Spell from the wand

**Effect** You make yourself the center of attention. An illusory spotlight shines bright light upon your space as you pull inane objects from the wand's tip, such as confetti, silk flowers, streamers, or a long string of colorful kerchiefs knotted end to end. Each enemy within 30 feet must attempt a Will save against your spell DC, receiving a +4 circumstance bonus to the save if you or any of your allies recently threatened it or used hostile actions against it. On a failure, the creature becomes [[Fascinated]] with you until the end of your next turn. The fascination ends if the target is subject to a hostile act, or if another creature succeeds at a Diplomacy or Intimidation check against it.

The spotlight follows you wherever you move. You can't be [[Concealed]] while in the spotlight. The effect ends if you become [[Invisible]], attempt a Stealth check, or Dismiss the activation.

You can Sustain this Activation for up to 1 minute. Since you need to keep performing tricks, Sustain an Activation has the manipulate trait. Sustaining extends the spotlight, and keeps fascinated creatures fascinated, but doesn't cause creatures not already fascinated to become fascinated.

**Craft Requirements** Supply a casting of a spell of the appropriate rank.

**Source:** `= this.source` (`= this.source-type`)
