---
type: creature
group: ["Humanoid", "Shadow"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Wayang Whisperblade"
level: "1"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Humanoid"
trait_02: "Shadow"
trait_03: "Wayang"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Darkvision]]"
languages: "Common, Shadowtongue, Wayang"
skills:
  - name: Skills
    desc: "Acrobatics +7, Deception +4, Occultism +6, Performance +6, Stealth +7, Thievery +7, Netherworld Lore +6"
abilityMods: ["+0", "+4", "+1", "+3", "+0", "+1"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The wayang deals an extra 1d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "16; **Fort** +6, **Ref** +9, **Will** +5"
health:
  - name: HP
    desc: "19"
abilities_mid:
  - name: "+1 Status to All Saves vs. Darkness or Shadow"
    desc: ""
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Kukri +8 (`pf2:1`) (agile, finesse, trip), **Damage** 1d6 slashing"
spellcasting: []
abilities_bot:
  - name: "Shadowplay"
    desc: "`pf2:1` **Requirements** The wayang's last action was a melee Strike that damaged their opponent <br>  <br> **Effect** The wayang attempts to [[Tumble Through]] the opponent's space, with a +2 circumstance bonus to the Acrobatics check. If they succeed, the wayang leaves a shadowy afterimage in their original space, which provides flanking against the opponent until the beginning of the wayang's next turn (usually making them [[Off Guard]] to the wayang's melee attacks)."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Some wayangs make use of their connections to shadows to outmaneuver their foes in combat.

In hushed tones, superstitious people tell their children stories of wayangs—living shadows who come out at night to eat misbehaving children. Mostly, these stories are just fictions of fearful minds, but it's true that wayangs were originally creatures of shadow, straddling the edge between light and darkness. The ancestors of modern-day wayangs set out on a great exodus some 10,000 years ago, leaving their native Netherworld to seek out a new home. On Golarion, they found a great cataclysm had blocked out the sun behind a cloud of smoke and ash, enshrouding the planet in a seemingly endless night, and here they made their new home. When the light returned, wayangs retreated into what shadowy places they could find, avoiding contact with humans and other peoples of the light, who viewed the small, gaunt beings as suspicious reminders of difficult times.

Many wayang groups are nomadic, though other groups have settled communities. Some live in homes carved out of natural caves, where they create works of art from stalagmites and other natural features. Others live in treetop villages in rainforests where sunlight barely penetrates the thick canopy of the forest. Wayangs are most populous in southeastern Tian Xia, especially in the archipelago of Minata, also known as the Wandering Isles, but their travels can sometimes take them to even further lands.

Despite their sinister reputation and secretive nature, wayangs are joyous creatures who tell stories and express their emotions through whisper-singing, dancing, and shadow puppetry, enhancing their performances with shadow magic. Similarly, they weave shadow magic into their deadly fighting styles, but wayangs aren't a violent people, usually fighting only to protect what's theirs. Wayangs decorate their stringy hair with beads and their dusky skin with tattooed white dots that form pictures, with each picture silently telling stories about their family's history or their worship of various deities of shadow.

```statblock
creature: "Wayang Whisperblade"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
