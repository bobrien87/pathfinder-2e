---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Doprillu"
level: "14"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+22; [[Darkvision]], [[See Invisibility]]"
languages: "Aklo, Common, Sakvroth"
skills:
  - name: Skills
    desc: "Acrobatics +26, Athletics +30, Intimidation +22, Stealth +24"
abilityMods: ["+8", "+6", "+7", "+1", "+4", "+2"]
abilities_top:
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
armorclass:
  - name: AC
    desc: "36; **Fort** +27, **Ref** +28, **Will** +24"
health:
  - name: HP
    desc: "260; regeneration 20 (deactivated by cold); **Resistances** fire 15"
abilities_mid:
  - name: "+2 Status Bonus to Saves vs. Fear"
    desc: ""
  - name: "Regeneration 20 (Deactivated by Cold)"
    desc: "This monster regains the listed number of Hit Points each round at the beginning of its turn. Its [[Dying]] condition never increases beyond Dying 3 as long as its regeneration is active. However, if it takes damage of a type listed in the regeneration entry, its regeneration deactivates until the end of its next turn. Deactivate the regeneration before applying any damage of a listed type, since that damage might kill the monster by bringing it to Dying 4."
  - name: "Deflect Arrow"
    desc: "`pf2:r` **Trigger** The doprillu is the target of a physical ranged attack <br>  <br> **Requirements** The doprillu is aware of the attack, isn't [[Off Guard]] against it, and has a hand free <br>  <br> **Effect** The doprillu gains a +4 circumstance bonus to its AC against the triggering attack."
  - name: "Mask of Power"
    desc: "A doprillu's unique wooden mask is the source of its power. <br>  <br> A doprillu deprived of its mask loses its regeneration and its immunity to Enfeebled and [[Slowed]], and it immediately becomes [[Enfeebled]] 1. The Enfeebled value increases by 1 at the start of each of the doprillu's turns, to a maximum of Enfeebled 4. If the mask is put back on, the doprillu immediately regains its abilities and loses the Enfeebled condition. <br>  <br> A creature can pull off the mask with a successful Athletics check to `act force-open dc=34`."
  - name: "Volcanic Veins"
    desc: "Fiery magma runs through the doprillu's veins. A creature that starts its turn [[Grabbed]] by the doprillu takes 7d6 fire damage."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +30 (`pf2:1`) (agile, magical, unarmed), **Damage** 3d8+16 bludgeoning plus 2d6 fire plus [[Improved Grab]]"
  - name: "Melee strike"
    desc: "Body Strike +30 (`pf2:1`) (magical, reach 10 ft.), **Damage** 3d8+16 bludgeoning"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 28, attack +18<br>**2nd** [[See the Unseen]] (Constant)"
abilities_bot:
  - name: "Whirlwind Throw"
    desc: "`pf2:2` **Requirements** The doprillu has a creature [[Grabbed]] <br>  <br> **Effect** The doprillu whirls the grabbed creature about, making a Body Strike against each creature in reach. After that Strike, the doprillu can hurl the grabbed creature up to 50 feet as a ranged Strike. This Strike has the same attack modifier and damage as Body Strike, but has the thrown 20 feet weapon trait."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The aberrations known as doprillus are hulks with banded muscles who wear ornate masks at all times that fill their wearers with magical strength and fighting spirit. Doprillus love to battle, especially by grappling, and are eager to start brawls. On neutral ground, a doprillu offers to duel the strongest-looking opponent, but when a doprillu's home turf is invaded, no rules apply to the confrontation. As befits the superheated blood that fuels them, doprillus make their homes in warm locations: hot jungles, sunny deserts, and underground caverns near sulfur vents.

```statblock
creature: "Doprillu"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
