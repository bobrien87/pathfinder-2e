---
type: creature
group: ["Human", "Humanoid"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Juggernaut"
level: "13"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Human"
trait_02: "Humanoid"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+21; [[Darkvision]]"
languages: "Common"
skills:
  - name: Skills
    desc: "Athletics +27, Crafting +26, Intimidation +26, Engineering Lore +24"
abilityMods: ["+8", "+3", "+4", "+2", "+2", "+2"]
abilities_top:
  - name: "Integrated Weapon"
    desc: "A juggernaut's armor includes one integrated melee weapon, such as a diamond-tipped rotary saw blade, massive pneumatic drill, or heavy spiked gauntlet. The specifics don't change the damage dealt by its Strikes, but determines whether it deals bludgeoning, piercing, or slashing damage. A juggernaut with tools and a workshop can spend 2 hours to swap their armor's integrated weapon."
  - name: "Power Source"
    desc: "Juggernaut armor requires a power source built into the armor—such as a steam boiler, Stasian coil, or alchemical reservoir. This determines a damage type—cold, electricity, fire, or poison—for certain abilities."
armorclass:
  - name: AC
    desc: "33; **Fort** +25, **Ref** +19, **Will** +21"
health:
  - name: HP
    desc: "250"
abilities_mid:
  - name: "Galvanized Plating"
    desc: "The juggernaut has resistance 10 to the damage type of the armor's power source."
  - name: "Self-Destruct"
    desc: "`pf2:r` **Trigger** The juggernaut is reduced to 0 Hit Points <br>  <br> **Effect** The juggernaut collapses and their armor emits a steady ticking sound. At the beginning of what would have been the juggernaut's next turn, the armor's power source explodes, destroying it completely and dealing @Damage[10d6[@actor.flags.system.powerSource]|options:area-damage] damage in a @Template[type:emanation|distance:30] with a DC 33 [[Reflex]] save. The explosion deals the damage type of the armor's power source. An adjacent creature can cancel the self-destruct sequence by succeeding at a DC 33 Thievery check to `act disable-device dc=33`."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Integrated Weapon +27 (`pf2:1`), **Damage** 3d8+12 untyped"
  - name: "Melee strike"
    desc: "Plated Fist +27 (`pf2:1`), **Damage** 3d4+14 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Energy Projector"
    desc: "`pf2:2` A juggernaut carries a powerful cannon-like projectile weapon that requires two hands to wield and deals @Damage[14d6[@actor.flags.system.powerSource]|options:area-damage] damage to all creatures in its area with a DC 31 basic save; the damage type, area, and save are based on the armor's power source, as listed below. Once activated, Energy Projector can't be used again for 1d4 rounds. <br>  <br> - **Cold** @Template[type:cone|distance:30] of cold ([[Reflex]] save) <br> - **Electricity** @Template[type:line|distance:60] of electricity ([[Reflex]] save) <br> - **Fire** @Template[type:cone|distance:30] of fire ([[Reflex]] save) <br> - **Poison** @Template[type:cone|distance:30] of poison gas ([[Fortitude]] save)"
  - name: "Jump Jets"
    desc: "`pf2:1` The juggernaut gains a Fly speed of 15 feet until the end of their current turn. If the juggernaut isn't on solid ground when they lose their fly Speed, they fall. After the effect ends, the juggernaut can't use Jump Jets again for 1 round."
  - name: "Trample"
    desc: "`pf2:3` Medium or smaller, plated fist, DC 33 [[Reflex]] save <br>  <br> The monster Strides up to double its Speed and can move through the spaces of creatures of the listed size, Trampling each creature whose space it enters. The monster can attempt to Trample the same creature only once in a single use of Trample. The monster deals the damage of the listed Strike, but trampled creatures can attempt a basic Reflex save at the listed DC (no damage on a critical success, half damage on a success, double damage on a critical failure)."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

The heavy suit of mechanical metal armor a juggernaut wears is custom-built and highly complex and specialized to its wearer. Other creatures can't make use of the armor unless they have similar skill and customize it thoroughly.

Although relatively uncommon across much of Golarion, the frequently eccentric but undeniably brilliant minds who create elaborate devices of clockwork, gunpowder, and steam often loom much larger in the public eye than their numbers would suggest.

```statblock
creature: "Juggernaut"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
