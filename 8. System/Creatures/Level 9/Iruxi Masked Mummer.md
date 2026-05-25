---
type: creature
group: ["Humanoid", "Lizardfolk"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Iruxi Masked Mummer"
level: "9"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Lizardfolk"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18"
languages: "Common, Draconic, Iruxi, Thalassic"
skills:
  - name: Skills
    desc: "Acrobatics +17, Athletics +17, Intimidation +19, Nature +18, Performance +20, Society +16, Survival +18, Iruxi Lore +20"
abilityMods: ["+2", "+4", "+0", "+1", "+3", "+4"]
abilities_top:
  - name: "Deep Breath"
    desc: "An iruxi masked mummer can hold their breath for 20 minutes."
armorclass:
  - name: AC
    desc: "27; **Fort** +15, **Ref** +19, **Will** +18"
health:
  - name: HP
    desc: "155"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tail +20 (`pf2:1`) (finesse, sweep, unarmed), **Damage** 2d6+8 bludgeoning"
  - name: "Melee strike"
    desc: "Claw +20 (`pf2:1`) (agile, finesse, unarmed, versatile p), **Damage** 2d4+8 slashing"
  - name: "Ranged strike"
    desc: "Spectral Roar +19 (`pf2:1`) (primal, sonic), **Damage** 3d10 sonic"
spellcasting: []
abilities_bot:
  - name: "Don Mask"
    desc: "`pf2:3` **Frequency** once per 10 minutes <br>  <br> **Effect** The mummer dons a ceremonial skull mask, calling an ancestral spirit to come to their aid. The spirit answers with a spell the mummer can cast as a primal innate spell (5th rank, DC 27) as part of the Don Mask activity. The mummer also gains a primal boon that lasts for 1 minute. After the minute is over or the mask is removed, the spell and boon end if either is still active, and the mummer is [[Fatigued]]. The most common legendary spirits the masks can invoke are: <br>  <br> - **Fiery Akkarok** (tyrannosaurus mask) <br>  <br> - **Spell** [[Blazing Bolt]] (3-action version) <br> - **Boon** The mummer's melee Strikes deal an additional 2d6 fire damage. <br>  <br> - **Hazi Zephyr-Borne** (griffon or iruxi mask) <br>  <br> - **Spell** [[Wall of Wind]] <br> - **Boon** The mummer gains a fly Speed of 20 feet. <br>  <br> - **King of Storms** (roc or horned dragon mask) <br>  <br> - **Spell** [[Howling Blizzard]] <br> - **Boon** The mummer gains the [[Reactive Strike]] reaction that can be used only with their tail. <br>  <br> - **Nessek, the Wave Dancer** (mosasaur mask) <br>  <br> - **Spell** [[Slither]] <br> - **Boon** The mummer's claw Strikes deal an additional 2d4 persistent bleed damage. <br>  <br> - **Zalok, Who was Called to Black Harbor** (naga or spinosaurus mask) <br>  <br> - **Spell** [[Hydraulic Torrent]] <br> - **Boon** The mummer gains a +10-foot status bonus to their land Speed and swim Speed."
  - name: "Starry Presence"
    desc: "`pf2:1` 30 feet. With a quick dance, the iruxi masked mummer surrounds themself with a starlight image resembling a figure from legend. The image lasts until the start of the mummer's next turn. An enemy that enters or starts its turn in the aura must succeed at a DC 25 [[Will]] save or become [[Dazzled]] until the start of its next turn."
sourcebook: "NPC Core"
source-type: "Remaster"
---
### `= this.file.name`

Iruxi masked mummers bring lizardfolk myths to life, donning elaborate costumes and bone masks to enact stories featuring their ancestors, the gods, legendary dragons and dinosaurs, and nature spirits of all kinds.

The most talented mummers claim their ritual dances invite these spirits inside them, suffusing their bodies with starlight and lending them primal power uniquely tied to the luminaries their masks represent. This magic can be seen even by those without magical ability, as they can see glowing motes shaped like distant stars seeming to float under the skin of the mummer.

Lizardfolk culture has flowered in recent years. With that revival has come a new generation of iruxis (as they call themselves) more willing to engage with the wider world, bringing with them their society's reverence for the past, facility with nature, and willingness to defend itself.

```statblock
creature: "Iruxi Masked Mummer"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
